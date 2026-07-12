function ChatPage() {
  return (
    <div className="min-h-screen bg-slate-950 text-white flex flex-col">

      <div className="border-b border-slate-800 p-6">

        <h1 className="text-3xl font-bold text-blue-400">
          RepoMind Chat
        </h1>

      </div>

      <div className="flex-1 flex justify-center items-center">

        <div className="text-center">

          <h2 className="text-4xl font-bold">
            Repository Ready ✅
          </h2>

          <p className="text-slate-400 mt-4">
            Your repository has been analyzed.
          </p>

          <p className="text-slate-500 mt-2">
            Tomorrow we'll build the ChatGPT interface.
          </p>

        </div>

      </div>

    </div>
  );
}

export default ChatPage;