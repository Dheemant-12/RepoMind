import { Github } from "lucide-react";
import { motion } from "framer-motion";

function LandingPage() {
  return (
    <div className="min-h-screen bg-slate-950 text-white">

      {/* Navbar */}

      <nav className="flex items-center justify-between px-10 py-6 border-b border-slate-800">

        <h1 className="text-3xl font-bold text-blue-400">
          RepoMind
        </h1>

        <button className="bg-blue-600 hover:bg-blue-700 px-5 py-2 rounded-lg transition">

          GitHub

        </button>

      </nav>

      {/* Hero */}

      <section className="flex flex-col items-center justify-center text-center mt-28">

        <motion.h1
          initial={{ opacity: 0, y: 40 }}
          animate={{ opacity: 1, y: 0 }}
          transition={{ duration: 0.7 }}
          className="text-6xl font-extrabold"
        >
          Chat With Any
          <br />
          GitHub Repository
        </motion.h1>

        <p className="text-slate-400 text-xl mt-6 max-w-2xl">

          Upload or paste a GitHub repository URL and ask AI
          anything about the codebase.

        </p>

        <div className="flex gap-3 mt-12 w-full max-w-4xl px-6">

          <input
            className="flex-1 rounded-xl border border-slate-700 bg-slate-900 px-6 py-4 outline-none focus:border-blue-500"
            placeholder="https://github.com/user/repository"
          />

          <button className="bg-blue-600 hover:bg-blue-700 rounded-xl px-8 flex items-center gap-2 transition">

            <Github size={20} />

            Analyze

          </button>

        </div>

      </section>

    </div>
  );
}

export default LandingPage;