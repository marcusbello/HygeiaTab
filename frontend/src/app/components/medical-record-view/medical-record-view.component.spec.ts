import { ComponentFixture, TestBed } from '@angular/core/testing';

import { MedicalRecordViewComponent } from './medical-record-view.component';

describe('MedicalRecordViewComponent', () => {
  let component: MedicalRecordViewComponent;
  let fixture: ComponentFixture<MedicalRecordViewComponent>;

  beforeEach(() => {
    TestBed.configureTestingModule({
      declarations: [MedicalRecordViewComponent]
    });
    fixture = TestBed.createComponent(MedicalRecordViewComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
