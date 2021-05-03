import { Injectable } from "@angular/core";
import {HttpClient } from "@angular/common/http";

@Injectable({providedIn:'root'})
export class AuthService {
    constructor(private http :HttpClient){}


    signUp(email : String , password : String){

        return this.http.post('http://127.0.0.1:8000/simple/UserDetail',
        {
            email:email,
            password:password

        });
    }

}