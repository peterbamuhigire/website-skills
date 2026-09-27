#!/usr/bin/env node
// Fail closed when a gate's local tool is not an exact, lockfile-backed direct dependency.
import fs from 'node:fs';
import path from 'node:path';
import process from 'node:process';

const root = process.cwd();
const manifestPath = path.join(root, 'package.json');
const lockPath = path.join(root, 'package-lock.json');
const manifest = fs.existsSync(manifestPath) ? JSON.parse(fs.readFileSync(manifestPath, 'utf8')) : null;
const lock = fs.existsSync(lockPath) ? JSON.parse(fs.readFileSync(lockPath, 'utf8')) : null;

if (!manifest || !lock || !lock.packages?.['']) {
  console.error('qa-tools: consuming project package.json and package-lock.json are required; install and lock QA tools in the project first.');
  process.exit(2);
}

let failed = false;
for (const spec of process.argv.slice(2)) {
  const separator = spec.lastIndexOf('=');
  if (separator < 1 || separator === spec.length - 1) {
    console.error(`qa-tools: invalid tool mapping '${spec}', expected package=binary`);
    failed = true;
    continue;
  }
  const name = spec.slice(0, separator);
  const binary = spec.slice(separator + 1);
  const declared = manifest.devDependencies?.[name] ?? manifest.dependencies?.[name];
  const lockedRoot = lock.packages[''].devDependencies?.[name] ?? lock.packages[''].dependencies?.[name];
  const installedPath = path.join(root, 'node_modules', ...name.split('/'), 'package.json');

  if (!declared || !/^\d+\.\d+\.\d+$/.test(declared)) {
    console.error(`qa-tools: ${name} must be a direct dependency at an exact stable version (currently ${declared ?? 'missing'}); review it, run npm audit, and commit package-lock.json.`);
    failed = true;
    continue;
  }
  if (lockedRoot !== declared || !fs.existsSync(installedPath) || JSON.parse(fs.readFileSync(installedPath, 'utf8')).version !== declared) {
    console.error(`qa-tools: ${name}@${declared} is not consistently installed from the project's lockfile; run npm ci.`);
    failed = true;
    continue;
  }
  if (binary !== '-' && !fs.existsSync(path.join(root, 'node_modules', '.bin', binary))) {
    const binPath = path.join(root, 'node_modules', '.bin', binary);
    console.error(`qa-tools: expected local executable ${binPath} for ${name}@${declared}.`);
    failed = true;
    continue;
  }
  console.log(`qa-tools: ${name}@${declared} resolved from the consuming project's exact lockfile.`);
}

if (failed) process.exit(2);
