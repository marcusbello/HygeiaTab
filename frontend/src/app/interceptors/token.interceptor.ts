import { Injectable } from '@angular/core';
import {
  HttpRequest,
  HttpHandler,
  HttpEvent,
  HttpInterceptor,
  HttpHeaders,
  HttpErrorResponse,
  HttpClient
} from '@angular/common/http';
import { Observable, catchError, switchMap, tap, throwError } from 'rxjs';
import { AuthService } from '../services/auth/auth.service';
import { environment } from 'src/environments/environment';
import { Router } from '@angular/router';

@Injectable()
export class TokenInterceptor implements HttpInterceptor {
  static accessToken = localStorage.getItem("accessToken")
  
  constructor(private httpClient: HttpClient, private router: Router) {
  }

  intercept(request: HttpRequest<unknown>, next: HttpHandler): Observable<HttpEvent<unknown>> {
    
    const bearer = `Bearer ${TokenInterceptor.accessToken}`;

    request = request.clone({
    headers: new HttpHeaders().set('Authorization', bearer)
    });

    // console.log(request)

    return next.handle(request).pipe(catchError((err: HttpErrorResponse) => {
      if (err.status === 401){
        // const access = localStorage.getItem('refreshToken')
        // return this.httpClient.post(environment.baseURL + 'token/refresh/', {"refresh":access}).pipe(
        //   switchMap((res: any) => {

        //     request = request.clone({
        //       headers: new HttpHeaders().set('Authorization', `Bearer ${res.access}`)
        //       });

        //     localStorage.setItem('accessToken', res.access)
        //     return next.handle(request)
        //   })
        // )
        this.router.navigate(['login'])
      }

      return throwError(() => err)
    }));
  }
}
