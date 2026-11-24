import test from "node:test";
import assert from "node:assert/strict";
import { formatBanner } from "./app.js";

test("formats banner with custom values", () => {
  assert.equal(formatBanner("Database", "HEALTHY"), "Database [HEALTHY]");
});

test("uses defaults when values are missing", () => {
  assert.equal(formatBanner("", ""), "PulseCheck [UP]");
});