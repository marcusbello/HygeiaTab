import { CanActivate, Router } from '@angular/router';
import { AuthService } from '../services/auth/auth.service';
import { Injectable } from '@angular/core';

@Injectable({
  providedIn: 'root'
})
export class isAuthenticatedGuard implements CanActivate {
  constructor(private authService: AuthService, private router: Router) {}

  canActivate(): boolean {
    const accessToken = localStorage.getItem('accessToken')

    if (accessToken) {
      // console.log('guard')
      return true;
    }

    // Access token is missing or expired, redirect to login
    this.router.navigate(['login']);
    return false;
  }
}


