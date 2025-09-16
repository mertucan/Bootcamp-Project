function Header() {
  return (
    <header className="flex items-center justify-center whitespace-nowrap border-b border-solid border-b-stone-200 dark:border-b-gray-700 px-10 py-4 relative">
      <div className="flex items-center gap-3 text-red-600 dark:text-red-500">
        <span className="material-symbols-outlined text-4xl"> fitness_center </span>
        <h1 className="text-2xl font-bold tracking-tighter">Personalized Workout Program Generator</h1>
      </div>
    </header>
  );
}

export default Header;
