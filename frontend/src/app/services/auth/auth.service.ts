import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { BehaviorSubject, Observable, tap } from 'rxjs';
import { environment } from 'src/environments/environment';
import { LoginRequest, LoginResponse } from 'src/app/models/login';
import jwt_decode from 'jwt-decode';

@Injectable({
  providedIn: 'root'
})
export class AuthService {

  private _isLoggedIn$ = new BehaviorSubject<boolean>(false)
  isLoggedIn$ = this._isLoggedIn$.asObservable();

  private apiUrl = environment.baseURL + '/login';
  constructor(private httpClient: HttpClient ) {
    const accessToken = localStorage.getItem('accessToken')
    this._isLoggedIn$.next(!!accessToken)
   }

  // login service
  login(formData: FormData): Observable<LoginResponse> {
    return this.httpClient.post<LoginResponse>(this.apiUrl, formData).pipe(
      tap((response: LoginResponse) => {
        localStorage.setItem('accessToken', response.access_token)
        this._isLoggedIn$.next(true)
      })
    )
    // return this.httpClient.post<LoginResponse>(this.apiUrl, req)
  }

 
  // getTokenExpiration(token: string): number | null {
  //   // const accessToken = this.getAccessToken();

  //   const decodedToken: any = jwt_decode(token);
  //   const expirationTime = decodedToken.exp * 1000; // Convert seconds to milliseconds
  //   return expirationTime;
  // }

  
}


