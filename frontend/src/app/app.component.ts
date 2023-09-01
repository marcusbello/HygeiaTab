import { Component } from '@angular/core';
import { AuthService } from './services/auth/auth.service';
import { Observable } from 'rxjs';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.scss']
})
export class AppComponent {
  title = 'HygeiaTab';

  constructor(public authService:AuthService) {
    // this.loggedIn$ = this.authService.isLoggedIn$
  }
}
