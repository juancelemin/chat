import { Component, OnInit } from '@angular/core';
import { NgForm } from '@angular/forms';
import {AuthService } from "./auth.service";
import {HttpClient } from "@angular/common/http";
import { FormsModule }   from '@angular/forms';


@Component({
  selector: 'app-auth',
  templateUrl: './auth.component.html',
  styleUrls: ['./auth.component.css']
})
export class AuthComponent implements OnInit {

  constructor(private authService: AuthService) { }

  ngOnInit(): void {
 
  }
  isLoginMode = true;
  
  onSwitchMode() {
    this.isLoginMode = !this.isLoginMode;
  }
  

  onSubmit(form: NgForm) {
    console.log(form.value);
    const userEmail = form.value.email;
    const userPassword = form.value.password;

    let val = this.authService.signUp(userEmail,userPassword).subscribe(
      resData => {
        console.log(resData);
      },
      error =>{
        console.log(error);
      }
    )
    form.reset();
  }


  login(form: NgForm) {
    console.log(form.value);
    const userEmail = form.value.email;
    const userPassword = form.value.password;

    let val = this.authService.login(userEmail,userPassword).subscribe(
      resData => {
        console.log(resData);
      },
      error =>{
        console.log(error);
      }
    )
    form.reset();
  }
}
