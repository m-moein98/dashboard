import axios from "axios";
import { Component } from "react";
import swal from "sweetalert";

class Error404 extends Component {
  render() {
    return (
      <div className="flex justify-center items-center bg-gradient-to-br from-blue-700 via-yellow-300 to-blue-700 m-auto min-h-screen">
        <div className="flex flex-col bg-indigo-200 w-5/6 sm:w-4/6 md:w-3/6 pt-14 md:pt-12 rounded-xl duration-500 ease-in-out transform hover:-translate-1 hover:scale-105">
          <div className="flex mb-10 mx-5">404 NOT FOUND </div>
        </div>
      </div>
    );
  }
}
export default Error404;
