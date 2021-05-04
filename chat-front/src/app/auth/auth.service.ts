import { Injectable } from "@angular/core";
import {HttpClient ,HttpParams} from "@angular/common/http";

@Injectable({providedIn:'root'})
export class AuthService {
    constructor(private http :HttpClient){}


    signUp(email : String , password : String){

        return this.http.post('http://127.0.0.1:8000/login/UserDetail',
        {
            email:email,
            password:password

        });
    }

    login(email : string , password : string){
        let params = new HttpParams().set('email', email).set('password', password);

        return this.http.get('http://127.0.0.1:8000/login/UserDetail',{params:params});
    }
    
    



}