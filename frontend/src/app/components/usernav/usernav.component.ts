import { Component, OnInit } from '@angular/core';
import { BehaviorSubject, Observable, tap } from 'rxjs';
import { User } from 'src/app/models/user';
import { AuthService } from 'src/app/services/auth/auth.service';
import { UserService } from 'src/app/services/user/user.service';

@Component({
  selector: 'app-usernav',
  templateUrl: './usernav.component.html',
  styleUrls: ['./usernav.component.scss']
})
export class UsernavComponent  {
 
  title = 'HygeiaTab';
  isDropdownOpen: boolean = false;
  isMenuHidden: boolean = true;

  constructor(private userService:UserService) {
    // this.getUserName()
  }

  toggleMenu() {
    this.isMenuHidden = !this.isMenuHidden;
  }

  toggleDropdown() {
    this.isDropdownOpen = !this.isDropdownOpen;
  }

  // getUserName(){
  //   this.userService.userInfo().pipe(
  //     tap((response: User) => {
  //       return response.first_name
  //     })
  //   )
  // }

 
}
