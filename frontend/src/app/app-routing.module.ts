import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { LoginComponent } from "./components/login/login.component";
import { MedicalRecordViewComponent } from "./components/medical-record-view/medical-record-view.component";
import { RegisterComponent } from "./components/register/register.component";
import { NotFoundComponent } from "./components/not-found/not-found.component";
import { HomeComponent } from './components/home/home.component';
import { DashboardComponent } from './components/dashboard/dashboard.component';
import { isAuthenticatedGuard } from './guards/is-authenticated.guard';
import { MedicalRecordsComponent } from './components/medical-records/medical-records.component';

const routes: Routes = [
  {path: '', redirectTo: 'home', pathMatch: 'full'},
  {path: 'home', component: HomeComponent},
  {path: 'login', component: LoginComponent},
  {path: 'register', component: RegisterComponent},
  {path: 'dashboard', component: DashboardComponent, canActivate: [isAuthenticatedGuard]},
  {path: 'medical-records', component: MedicalRecordsComponent, canActivate: [isAuthenticatedGuard]},
  {path: 'medical-record/:id', component: MedicalRecordViewComponent, canActivate: [isAuthenticatedGuard]},
  {path: 'medical-record/:medical_record_id/treatments/', component: MedicalRecordViewComponent, canActivate: [isAuthenticatedGuard]},
  {path: '**', component: NotFoundComponent},
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
