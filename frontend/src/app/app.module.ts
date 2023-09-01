import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';

import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { LoginComponent } from './components/login/login.component';
import {FormsModule, ReactiveFormsModule} from "@angular/forms";
import {HTTP_INTERCEPTORS, HttpClientModule} from "@angular/common/http";
import { MedicalRecordViewComponent } from './components/medical-record-view/medical-record-view.component';
import { RegisterComponent } from './components/register/register.component';
import { NotFoundComponent } from './components/not-found/not-found.component';
import { NavbarComponent } from './components/navbar/navbar.component';
import { HomeComponent } from './components/home/home.component';
import { DashboardComponent } from './components/dashboard/dashboard.component';
import { UsernavComponent } from './components/usernav/usernav.component';
import { isAuthenticatedGuard } from './guards/is-authenticated.guard';
import { TokenInterceptor } from './interceptors/token.interceptor';
import { MedicalRecordsComponent } from './components/medical-records/medical-records.component';

@NgModule({
  declarations: [
    AppComponent,
    LoginComponent,
    MedicalRecordViewComponent,
    RegisterComponent,
    NotFoundComponent,
    NavbarComponent,
    HomeComponent,
    DashboardComponent,
    UsernavComponent,
    MedicalRecordsComponent
  ],
  imports: [
    BrowserModule,
    AppRoutingModule,
    FormsModule,
    ReactiveFormsModule,
    HttpClientModule
  ],
  providers: [
    isAuthenticatedGuard,
    {
      provide: HTTP_INTERCEPTORS,
      useClass: TokenInterceptor,
      multi: true
    }
    ],
  bootstrap: [AppComponent]
})
export class AppModule { }
