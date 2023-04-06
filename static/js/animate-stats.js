function animateValue(id, start, end, duration) {
  const range = end - start;
  let current = start;
  const increment = end > start ? 1 : -1;
  const stepTime = Math.abs(Math.floor(duration / range));
  const element = document.getElementById(id);

  const timer = setInterval(() => {
    current += increment;
    element.textContent = current;
    if (current === end) {
      clearInterval(timer);
    }
  }, stepTime);
}

function fetchStats() {
  $.ajax({
    url: "/argusthedorker/stats", // Replace this with the actual API endpoint URL
    method: "GET",
    dataType: "json",
    success: function (data) {
      // Update the stats with the fetched data
      animateValue("dorks-count", 0, data.dorks_count, 2000);
      animateValue("urls-count", 0, data.urls_count, 2000);
      animateValue("domains-count", 0, data.domains_count, 2000);
    },
    error: function (error) {
      console.error("Error fetching stats:", error);
    },
  });
}

$(document).ready(function () {
  fetchStats();
});
