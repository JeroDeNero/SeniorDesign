import { Injectable } from '@angular/core';
import { Socket } from 'ngx-socket-io';
import { BehaviorSubject, Observable, Observer } from 'rxjs';

@Injectable({
  providedIn: 'root',
})
export class StreamService {
  primaryCam: BehaviorSubject<any> = new BehaviorSubject<any>('');

  constructor(private socket: Socket) {}

  ngOnInit() {}

  setPrimaryCam(image: any): void {
    this.primaryCam.next(image);
  }

  watchVideo() {
    return new Observable((observer: Observer<any>) => {
      this.socket.on('primaryStreamOut', (data) => {
        observer.next(data);
      });
    });
  }
}
