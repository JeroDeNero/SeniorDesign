import { Injectable } from '@angular/core';
import { BehaviorSubject, Observable, ReplaySubject } from 'rxjs';
import { delay } from 'rxjs/operators';
import { RunService } from './run.service';

@Injectable({
  providedIn: 'root',
})
export class ToggleService {
  hideNew: BehaviorSubject<boolean> = new BehaviorSubject<boolean>(true);
  hideEdit: BehaviorSubject<boolean> = new BehaviorSubject<boolean>(true);

  showFavorites: BehaviorSubject<boolean> = new BehaviorSubject<boolean>(true);
  showNamed: BehaviorSubject<boolean> = new BehaviorSubject<boolean>(true);
  showUnamed: BehaviorSubject<boolean> = new BehaviorSubject<boolean>(true);

  resetFilter: BehaviorSubject<boolean> = new BehaviorSubject<boolean>(true);

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
      this.runService.addRun().subscribe();
      this.setButtonOp('New Run');
    }
  }

  toggleResetFilter() {
    this.resetFilter.next(!this.resetFilter.getValue());
    setTimeout(() => {
      this.resetFilter.next(!this.resetFilter.getValue());
    }, 1);
  }

  getResetFilter() {
    return this.resetFilter.asObservable();
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

  setShowFavorites(value) {
    this.showFavorites.next(value);
  }

  getShowFavorites() {
    return this.showFavorites.asObservable();
  }

  setShowNamed(value) {
    this.showNamed.next(value);
  }

  getShowNamed() {
    return this.showNamed.asObservable();
  }

  setShowUnamed(value) {
    this.showUnamed.next(value);
  }

  getShowUnamed() {
    return this.showUnamed.asObservable();
  }
}
