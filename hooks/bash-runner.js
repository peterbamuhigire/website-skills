'use strict';

const fs = require('fs');
const path = require('path');
const { spawnSync } = require('child_process');

let cachedBash;

function resolveBashExecutable() {
  if (process.platform !== 'win32') return 'bash';
  if (cachedBash) return cachedBash;

  // Prefer a standard Git for Windows install. Windows also provides a
  // `bash.exe` launcher for WSL, but it cannot consume ordinary C:\ paths as
  // script arguments. Avoid discovering an executable through the project
  // PATH because a checkout could shadow `git.exe` with an adjacent Bash.
  const installRoots = [
    process.env.ProgramW6432,
    process.env.ProgramFiles,
    process.env['ProgramFiles(x86)'],
  ].filter(Boolean);
  for (const root of new Set(installRoots)) {
    const candidate = path.join(root, 'Git', 'bin', 'bash.exe');
    if (fs.existsSync(candidate)) {
      cachedBash = candidate;
      return cachedBash;
    }
  }

  // Do not fall through to the Windows WSL launcher: its Linux Bash cannot
  // consume this process's native Windows script paths. Callers already
  // classify a missing runtime as a non-blocking prerequisite skip.
  cachedBash = null;
  return cachedBash;
}

function runBash(scriptPath, args = [], options = {}) {
  const executable = resolveBashExecutable();
  if (!executable) {
    const error = new Error('Git Bash for Windows was not found under Program Files');
    error.code = 'ENOENT';
    return { status: null, error, stdout: null, stderr: null };
  }
  return spawnSync(executable, [scriptPath, ...args], options);
}

module.exports = { resolveBashExecutable, runBash };
