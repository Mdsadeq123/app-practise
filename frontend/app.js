import http from "node:http";

export function formatBanner(serviceName, status) {
  return `${serviceName || "PulseCheck"} [${status || "UP"}]`;
}

const server = http.createServer((req, res) => {
  res.writeHead(200, { "Content-Type": "text/plain" });
  res.end(formatBanner("PulseCheck API", "UP"));
});

if (process.env.NODE_ENV !== "test") {
  server.listen(3000, () => console.log("Frontend listening on 3000"));
}