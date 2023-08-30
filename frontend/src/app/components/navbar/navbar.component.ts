import { Component } from '@angular/core';

@Component({
  selector: 'app-navbar',
  templateUrl: './navbar.component.html',
  styleUrls: ['./navbar.component.scss']
})
export class NavbarComponent {
  title = 'HygeiaTab';
  isDropdownOpen: boolean = false;
  isMenuHidden: boolean = true;

  toggleMenu() {
    this.isMenuHidden = !this.isMenuHidden;
  }

  toggleDropdown() {
    this.isDropdownOpen = !this.isDropdownOpen;
  }
}
