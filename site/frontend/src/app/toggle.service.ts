import { Injectable } from '@angular/core';
import { BehaviorSubject, Observable, ReplaySubject } from 'rxjs';
import { RunService } from './run.service';

@Injectable({
  providedIn: 'root',
})
export class ToggleService {
  hideNew: BehaviorSubject<boolean> = new BehaviorSubject<boolean>(true);
  hideEdit: BehaviorSubject<boolean> = new BehaviorSubject<boolean>(true);

  buttonOp: BehaviorSubject<string> = new BehaviorSubject<string>('New Run');

  constructor(private runService: RunService) {}

  ngOnInit() {}

  operateNewWindow(): void {
    if (this.buttonOp.getValue() === 'New Run') {
      this.toggleHideNew();
      this.setButtonOp('');
    } else if (this.buttonOp.getValue() === '') {
      this.toggleHideNew();
      this.setButtonOp('End Run');
    } else {
      this.setButtonOp('New Run');
    }
  }

  toggleHideNew(): void {
    this.hideNew.next(!this.hideNew.getValue());
  }

  getHideNew(): Observable<boolean> {
    return this.hideNew.asObservable();
  }

  toggleHideEdit(): void {
    this.hideEdit.next(!this.hideEdit.getValue());
  }

  setHideEdit(targ): void {
    this.hideEdit.next(targ);
  }

  getHideEdit(): Observable<boolean> {
    return this.hideEdit.asObservable();
  }

  setButtonOp(word): void {
    this.buttonOp.next(word);
  }

  getButtonOp(): Observable<string> {
    return this.buttonOp.asObservable();
  }
}
