<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1" />
  <title>StartLeetCodewithMe — Journey</title>
  <script src="https://cdn.tailwindcss.com"></script>
  <script>
    tailwind.config = {
      theme: {
        extend: {
          colors: {
            primary: '#0ea5a4',
            accent: '#6366f1',
          }
        }
      }
    }
  </script>
</head>
<body class="bg-gray-50 text-gray-800 antialiased">
  <div class="min-h-screen flex items-center justify-center p-6">
    <div class="max-w-4xl w-full bg-white rounded-2xl shadow-lg ring-1 ring-gray-100 overflow-hidden">
      <header class="px-8 py-6 flex items-start justify-between">
        <div>
          <h1 class="text-2xl font-extrabold tracking-tight text-gray-900 flex items-center gap-3">
            <span class="inline-block w-10 h-10 bg-gradient-to-r from-primary to-accent rounded-full flex items-center justify-center text-white font-bold">SL</span>
            <span>StartLeetCodewithMe</span>
          </h1>
          <p class="mt-1 text-sm text-gray-500">Pattern-wise LeetCode journey — 3 problems/day • Starting 22nd</p>
        </div>
        <div class="space-x-3">
          <a href="#" class="inline-flex items-center gap-2 px-4 py-2 rounded-full bg-primary text-white text-sm font-semibold hover:brightness-95">⭐ Star</a>
          <a href="#" class="inline-flex items-center gap-2 px-4 py-2 rounded-full border border-gray-200 text-sm">View on GitHub</a>
        </div>
      </header>

      <main class="px-8 pb-8">
        <section class="grid md:grid-cols-2 gap-6 items-center">
          <div>
            <h2 class="text-3xl font-extrabold text-gray-900">A simple plan. Daily discipline. Big results.</h2>
            <p class="mt-4 text-gray-600">From <strong>22nd</strong>, I will solve <strong>3 problems every day</strong>, focused on one algorithmic pattern. This repo contains pattern folders, clean solutions, explanations, and progress notes.</p>

            <div class="mt-6 flex flex-wrap gap-3">
              <div class="px-4 py-2 bg-gray-100 rounded-full text-sm font-medium">Daily: 3 problems</div>
              <div class="px-4 py-2 bg-gray-100 rounded-full text-sm font-medium">Pattern-wise</div>
              <div class="px-4 py-2 bg-gray-100 rounded-full text-sm font-medium">Clean solutions</div>
            </div>

            <div class="mt-6 flex gap-3">
              <a href="#patterns" class="inline-block px-5 py-3 rounded-lg bg-accent text-white font-semibold">See patterns</a>
              <a href="#progress" class="inline-block px-5 py-3 rounded-lg border border-gray-200 text-sm">My progress</a>
            </div>
          </div>

          <div class="bg-gradient-to-br from-primary/10 to-accent/8 rounded-xl p-6">
            <div class="flex items-center gap-4">
              <div class="w-16 h-16 flex items-center justify-center bg-white rounded-lg shadow">📈</div>
              <div>
                <p class="text-sm text-gray-500">Goal</p>
                <p class="text-lg font-semibold text-gray-900">Build strong DSA skills</p>
              </div>
            </div>

            <div class="mt-6 grid grid-cols-3 gap-4">
              <div class="p-3 bg-white rounded-lg text-center">
                <p class="text-xs text-gray-500">Daily</p>
                <p class="font-bold text-xl">3</p>
              </div>
              <div class="p-3 bg-white rounded-lg text-center">
                <p class="text-xs text-gray-500">Start Date</p>
                <p class="font-bold text-xl">22nd</p>
              </div>
              <div class="p-3 bg-white rounded-lg text-center">
                <p class="text-xs text-gray-500">Pattern</p>
                <p class="font-bold text-xl">Focused</p>
              </div>
            </div>

            <p class="mt-6 text-sm text-gray-500">Notes: Each pattern folder has 3 solutions per day with explanations and key takeaways.</p>
          </div>
        </section>

        <section id="patterns" class="mt-8">
          <h3 class="text-xl font-semibold">Patterns (example)</h3>
          <div class="mt-4 grid sm:grid-cols-3 gap-4">
            <article class="p-4 bg-white rounded-lg shadow-sm">
              <h4 class="font-semibold">Two Pointers</h4>
              <p class="text-sm text-gray-500 mt-2">Sliding window, sorted arrays — 3 problems per day.</p>
            </article>
            <article class="p-4 bg-white rounded-lg shadow-sm">
              <h4 class="font-semibold">Binary Search</h4>
              <p class="text-sm text-gray-500 mt-2">Classic & variant problems with explanation.</p>
            </article>
            <article class="p-4 bg-white rounded-lg shadow-sm">
              <h4 class="font-semibold">Dynamic Programming</h4>
              <p class="text-sm text-gray-500 mt-2">State definition, transitions, and optimization notes.</p>
            </article>
          </div>
        </section>

        <section id="progress" class="mt-8">
          <h3 class="text-xl font-semibold">Progress tracker</h3>
          <div class="mt-4 bg-white rounded-lg p-4 shadow-sm">
            <div class="flex items-center justify-between">
              <div>
                <p class="text-sm text-gray-500">Days completed</p>
                <p class="text-2xl font-bold">0</p>
              </div>
              <div>
                <p class="text-sm text-gray-500">Problems solved</p>
                <p class="text-2xl font-bold">0</p>
              </div>
            </div>
            <p class="mt-4 text-sm text-gray-500">Update these numbers in the repo README or a simple JSON file to keep the tracker live.</p>
          </div>
        </section>

        <footer class="mt-8 border-t pt-6 flex flex-col sm:flex-row items-start sm:items-center justify-between gap-4">
          <p class="text-sm text-gray-500">Made with focus • Keep it consistent — Noman</p>
          <div class="flex items-center gap-3">
            <a href="#" class="text-sm px-3 py-2 border rounded-lg">Contribute</a>
            <a href="#" class="text-sm px-3 py-2 bg-primary text-white rounded-lg">Download HTML</a>
          </div>
        </footer>
      </main>
    </div>
  </div>
</body>
</html>
