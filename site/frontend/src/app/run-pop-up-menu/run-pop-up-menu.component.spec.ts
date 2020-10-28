import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { RunPopUpMenuComponent } from './run-pop-up-menu.component';

describe('RunPopUpMenuComponent', () => {
  let component: RunPopUpMenuComponent;
  let fixture: ComponentFixture<RunPopUpMenuComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [RunPopUpMenuComponent],
    }).compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(RunPopUpMenuComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
