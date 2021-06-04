const Navbar = () => {
    return (
        <div className="flex justify-center items-center h-0">
            <div className="flex justify-center sm:justify-between bg-indigo-200 text-graye-800 w-5/6 pt-14 pb-1.5 rounded-xl">
                <button className="bg-yellow-300 ml-4 p-2 px-8 sm:px-4 focus:outline-none rounded-bl-xl sm:rounded-full duration-500 ease-in-out transform hover:-translate-1 hover:scale-125">&#60;</button>
                <button className="bg-yellow-300 p-2 px-8 focus:outline-none duration-500 sm:rounded ease-in-out transform hover:-translate-1 hover:scale-110">home</button>
                <button className="bg-yellow-300 mr-4 p-2 px-8 sm:px-4 focus:outline-none rounded-br-xl sm:rounded-full duration-500 ease-in-out transform hover:-translate-1 hover:scale-125">&#62;</button>
            </div>
        </div>
    )
};
export default Navbar;