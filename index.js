const http = require("http");
const { spawn } = require("child_process");

const server = http.createServer((req, res) => {
  const process = spawn("python", ["run.py"]);

  process.stdout.on("data", (data) => {
    res.write(data);
  });

  process.stderr.on("data", (data) => {
    res.write(data);
  });

  process.on("close", () => {
    res.end();
  });
});

server.listen(process.env.PORT || 3000);