import { DatePipe } from '@angular/common';
import { Component } from '@angular/core';
import { Observable } from 'rxjs';
import { MedicalRecord } from 'src/app/models/medical-record';
import { MedicalRecordService } from 'src/app/services/medical_record/medical-record.service';

@Component({
  selector: 'app-medical-records',
  templateUrl: './medical-records.component.html',
  styleUrls: ['./medical-records.component.scss'],
  providers: [DatePipe]
})
export class MedicalRecordsComponent {

  
  medicalRecords$: Observable<MedicalRecord[]> | undefined;

  constructor(private medicalRecordService: MedicalRecordService, private datePipe: DatePipe) {}

  ngOnInit(): void {
    this.medicalRecords$ = this.medicalRecordService.getMedicalRecords();
  }


  convertToReadableTime(time: Date): string | null {
    if(!time){
      return '';
    }
    const date = new Date(time);
    return this.datePipe.transform(date, 'dd MMMM, yyyy @ hh:mma');
  }


}
