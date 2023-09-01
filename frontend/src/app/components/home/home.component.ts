import { Component, OnInit } from '@angular/core';
import { Router } from '@angular/router';
import { Observable } from 'rxjs';
import { AuthService } from 'src/app/services/auth/auth.service';

@Component({
  selector: 'app-home',
  templateUrl: './home.component.html',
  styleUrls: ['./home.component.scss']
})
export class HomeComponent {
  loggedIn$: Observable<boolean>;

  constructor (private authService: AuthService, private router:Router) {
    this.loggedIn$ = this.authService.isLoggedIn$
  }

  isLoggedIn() {
    this.router.navigate(['/dashboard'])
  }

  heading = 'Tracking your medical records have never been easier.';
  subHeading = 'Experience the convenience of signing up and taking control of your medical records for a healthier and more organized future.';

  features: Feature[] = [
    { title: 'Secure and Centralized Storage', description: 'Safely store and manage your medical records in one place, ensuring the privacy of your sensitive information.' },
    { title: 'Easy Record Retrieval', description: 'Instantly access your medical records anytime, anywhere with our intuitive search functionality.' },
    { title: 'Appointment Management', description: 'Seamlessly schedule, track, and receive reminders for your medical appointments.Stay on top of your healthcare routine and never miss an important visit again.' },
    { title:'Medication Tracker', description: 'Keep track of your medications, dosage instructions, and refill schedules in one convenient location. Set reminders to take medications on time and avoid missing any doses.'},
    { title:'Family Health Management', description: 'Easily manage the medical records of your family members or dependents, ensuring seamless coordination and access to vital health information when needed.'},
    { title:'Emergency Access', description: ' In case of emergencies, grant designated individuals immediate access to your medical records. Provide essential information and instructions that can aid healthcare professionals in delivering appropriate care.'},
  ];

}

interface Feature {
  title: string;
  description: string;
}
