import { Component, OnInit } from '@angular/core';
import { FormGroup, FormControl, Validators } from '@angular/forms';
import { RegisterRequest, RegisterResponse, RegisterError } from 'src/app/models/register';
import { UserService } from 'src/app/services/user/user.service';

@Component({
  selector: 'app-register',
  templateUrl: './register.component.html',
  styleUrls: ['./register.component.scss']
})
export class RegisterComponent implements OnInit {
   
   formGroup!: FormGroup;

   constructor( private userService:UserService) {
   }
   ngOnInit() {
     this.initForm();
   }
 
   initForm() {
     this.formGroup = new FormGroup<any>({
       first_name: new FormControl('', [Validators.required]),
       last_name: new FormControl('', [Validators.required]),
       email: new FormControl('', [Validators.required]),
       gender: new FormControl('',[Validators.required]),
       dob: new FormControl('',[Validators.required]),
       password: new FormControl('', [Validators.required]),
       confirmPassword: new FormControl('', [Validators.required]),
     })
   }


  register() {
    if(this.formGroup.valid){
      const registerRequest: RegisterRequest = {
        first_name: this.formGroup.value['name'],
        last_name: this.formGroup.value['name'],
        gender: this.formGroup.value['gender'],
        dob: this.formGroup.value['dob'],
        email: this.formGroup.value['email'],
        password: this.formGroup.value['password']
      };
      // login service
      this.userService.userCreate(registerRequest).subscribe(
        (response: RegisterResponse | RegisterError) => {
          
          // Handle successful login response
          console.log('Register successful');
          console.log('Data:', response);
          // Redirect to another page, set token in local storage, etc.
        },
        (error: RegisterError) => {
          // Handle error response
          console.log('Login error:', error.error);
          // Display error message to the user, show/hide error div, etc.
        }
      );
    }
  }



}

