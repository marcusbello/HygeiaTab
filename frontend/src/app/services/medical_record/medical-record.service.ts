import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { Observable } from 'rxjs';
import { environment } from 'src/environments/environment';
import { MedicalRecord } from 'src/app/models/medical-record'

@Injectable({
  providedIn: 'root'
})
export class MedicalRecordService {
  path = environment.baseURL + '/medical-record/'

  constructor(private httpClient: HttpClient) {
   }

  
  getMedicalRecords(): Observable<MedicalRecord[]> {
    return this.httpClient.get<MedicalRecord[]>(this.path)
  }

  getMedicalRecord(id: string | null): Observable<MedicalRecord> {
    return this.httpClient.get<MedicalRecord>(this.path + id)
  }
}
