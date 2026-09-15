async function updateMetrics() {
  try {
    const response = await fetch("/api/metrics");
    const data = await response.json();

    document.getElementById("hostname").textContent = data.hostname;
    document.getElementById("platform").textContent =
      `${data.os} ${data.os_version} · Python ${data.python}`;

    document.getElementById("cpu").textContent = data.cpu_percent;
    document.getElementById("memory").textContent = data.memory_percent;
    document.getElementById("disk").textContent = data.disk_percent;

    document.getElementById("cpu-bar").style.width = `${data.cpu_percent}%`;
    document.getElementById("memory-bar").style.width = `${data.memory_percent}%`;
    document.getElementById("disk-bar").style.width = `${data.disk_percent}%`;

    document.getElementById("os").textContent = `${data.os} ${data.os_version}`;
    document.getElementById("python").textContent = data.python;
    document.getElementById("updated").textContent = data.timestamp;
  } catch (error) {
    console.error("Unable to collect metrics:", error);
  }
}

updateMetrics();
setInterval(updateMetrics, 3000);
