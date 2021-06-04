import axios from "axios";
import { Component } from "react";
import swal from "sweetalert";

class Login extends Component {
    constructor(props) {
        super(props)
        this.state = {
            email: "",
            password: "",
            rePassword: ""
        }
        this.Submit = this.Submit.bind(this)
    }
    Submit() {
        if (this.state.username === "" || this.state.password === ""){
            swal("Please fill the form before submission")
        }else{
            axios.post('http://127.0.0.1:8000/api/auth/register', {
                username: this.state.email,
                email: this.state.email,
                password: this.state.password,
                rePassword: this.state.rePassword
            },
            )
            .then(function (response) {
                swal(String(response.data.success))
            })
            .catch(function (error) {
                swal("this email exists! try another one or login")
            })
        }

    }
    handleChange = (event) => {
        const name = event.target.name
        const value = event.target.value
        this.setState({
            [name]: value
        })
    }
    render() {
        return (
            <div className="flex justify-center items-center bg-gradient-to-br from-blue-700 via-yellow-300 to-blue-700 m-auto min-h-screen">
                <div className="flex flex-col bg-indigo-200 w-5/6 sm:w-4/6 md:w-3/6 pt-14 md:pt-12 rounded-xl duration-500 ease-in-out transform hover:-translate-1 hover:scale-105">
                    <img className="mx-auto w-32 my-2 pb-8 rounded-full transition duration-500 ease-in-out transform hover:-translate-1 hover:scale-110" src="https://picsum.photos/200" alt="" />
                    <input
                        className="mx-auto h-auto w-4/6 my-1 md:my-2 2xl:my-3 p-3 text-center text-lg md:text-xl text-gray-200 placeholder-white font-bold focus:outline-none transition duration-500 ease-in-out bg-blue-400 hover:bg-blue-300 hover:placeholder-red-500 transform hover:-translate-y-1 hover:scale-110" 
                        name="email" 
                        placeholder="email" 
                        type="email"
                        value={this.state.email}
                        onChange={this.handleChange}
                    />
                    <input
                        className="mx-auto h-auto w-4/6 my-1 md:my-2 2xl:my-3 p-3 text-center text-lg md:text-xl text-gray-200 placeholder-white font-bold focus:outline-none transition duration-500 ease-in-out bg-blue-400 hover:bg-blue-300 hover:placeholder-red-500 transform hover:-translate-y-1 hover:scale-110 " 
                        name="password" 
                        placeholder="password" 
                        type="password"
                        value={this.state.password}
                        onChange={this.handleChange}
                    />
                    <input
                        className="mx-auto h-auto w-4/6 my-1 md:my-2 2xl:my-3 p-3 text-center text-lg md:text-xl text-gray-200 placeholder-white font-bold focus:outline-none transition duration-500 ease-in-out bg-blue-400 hover:bg-blue-300 hover:placeholder-red-500 transform hover:-translate-y-1 hover:scale-110 " 
                        name="rePassword" 
                        placeholder="repeat password" 
                        type="password"
                        value={this.state.rePassword}
                        onChange={this.handleChange}
                    />
                    <button onClick={this.Submit} className="mx-auto h-auto w-4/6 my-2 p-3 mb-10 text-xl bg-blue-700 text-white transition duration-500 ease-in-out hover:bg-blue-600 transform hover:-translate-y-1 hover:scale-110">Login</button>
                </div>
            </div>
        )
    }
}
export default Login