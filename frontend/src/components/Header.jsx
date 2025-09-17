import { Link } from 'react-router-dom';

function Header() {
  return (
    <header className="flex items-center justify-between whitespace-nowrap border-b border-solid border-b-stone-200 dark:border-b-gray-700 px-10 py-4 relative">
      <Link to="/" className="flex items-center gap-3 text-red-600 dark:text-red-500">
        <span className="material-symbols-outlined text-4xl">fitness_center</span>
        <h1 className="text-2xl font-bold tracking-tighter">FitBit Coach</h1>
      </Link>
      <nav>
        <Link to="/my-activity" className="px-4 py-2 rounded-md hover:bg-stone-100 dark:hover:bg-gray-800 transition-colors text-stone-700 dark:text-gray-200 font-medium">
          My Activity
        </Link>
      </nav>
    </header>
  );
}

export default Header;
