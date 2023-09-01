import {Component, OnInit} from '@angular/core';
import {FormControl, FormGroup, Validators} from "@angular/forms";
import {AuthService} from "../../services/auth/auth.service";
import { LoginError, LoginRequest, LoginResponse } from 'src/app/models/login';
import { Token } from '@angular/compiler';
import { Router } from '@angular/router';

@Component({
  selector: 'app-login',
  templateUrl: './login.component.html',
  styleUrls: ['./login.component.scss']
})
export class LoginComponent implements OnInit {
  // @ts-ignore
  formGroup: FormGroup;

  constructor( private authService:AuthService, private router: Router) {
  }
  ngOnInit() {
    this.initForm();
  }

  initForm() {
    this.formGroup = new FormGroup<any>({
      email: new FormControl('', [Validators.required]),
      password: new FormControl('', [Validators.required]),
    })
  }

  // loginReq 
  login(){
    if(this.formGroup.valid){
      const formData = new FormData();
      formData.append('username', this.formGroup.value['email']);
      formData.append('password', this.formGroup.value['password']);
      // 
      // const loginRequest: LoginRequest = {
      //   username: this.formGroup.value['email'],
      //   password: this.formGroup.value['password']
      // };
      // login service
      this.authService.login(formData).subscribe(
        (response: LoginResponse) => {
          
          // Handle successful login response
          console.log('Login successful');
          console.log(response.access_token)
          this.router.navigate(['dashboard'])
          // Redirect to another page, set token in local storage, etc.
        },
        (error: LoginError) => {
          // Handle error response
          console.log('Login error:', error.error);
          // Display error message to the user, show/hide error div, etc.
        }
      );
    }
  }
}
