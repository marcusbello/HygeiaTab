import { DatePipe } from '@angular/common';
import {Component, OnInit} from '@angular/core';
import {ActivatedRoute} from "@angular/router";
import { Observable } from 'rxjs';
import { MedicalRecord } from 'src/app/models/medical-record';
import { MedicalRecordService } from 'src/app/services/medical_record/medical-record.service';

@Component({
  selector: 'app-medical-record-view',
  templateUrl: './medical-record-view.component.html',
  styleUrls: ['./medical-record-view.component.scss'],
  providers: [DatePipe]
})
export class MedicalRecordViewComponent implements OnInit{
  medicalRecord$: Observable<MedicalRecord> | undefined;

  paramQuery = '';
  constructor( 
    private route: ActivatedRoute,
    private medicalRecordService: MedicalRecordService,
    private datePipe: DatePipe
    ) { }

  ngOnInit() {
    const Id = this.route.snapshot.paramMap.get('id');
    this.medicalRecord$ = this.medicalRecordService.getMedicalRecord(Id);
  }

  convertToReadableTime(time: Date): string | null {
    if(!time){
      return '';
    }
    const date = new Date(time);
    return this.datePipe.transform(date, 'dd MMMM, yyyy @ hh:mma');
  }

}
