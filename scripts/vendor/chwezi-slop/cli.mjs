#!/usr/bin/env node
// Website entry point for the vendored chwezi-slop detector (M10-11-T01).
// The vendored files keep the design engine's layout so the detector can find
// hooks/lib/font-matcher.js and doctrine/references/ai-slop-banned-fonts.json.
// This shim only forwards to tools/slop-detector/cli.mjs; it is website-owned
// and is not part of the hash-checked set in VENDOR.json.
import './tools/slop-detector/cli.mjs';
