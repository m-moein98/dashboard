const Profile = () =>{
    return(
    <div className="flex justify-center items-center bg-gradient-to-br from-blue-700 via-yellow-300 to-blue-700 m-auto h-screen min-h-screen">
        <div className="flex flex-col bg-green-50 w-5/6 h-5/6 rounded-xl duration-500 ease-in-out">
            <img className="mx-auto w-30 my-1 md:my-2 2xl:my-3 md:mt-10 rounded-full transition duration-500 ease-in-out transform hover:-translate-1 hover:scale-110" src="https://picsum.photos/200" alt="" />
            <h1 className="text-center text-lg lg:text-xl xl:text-2xl font-bold">mr robot</h1>
        </div>
    </div>
    )
};
export default Profile;