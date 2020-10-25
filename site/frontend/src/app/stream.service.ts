import { Injectable } from '@angular/core';
import { Socket } from 'ngx-socket-io';
import { BehaviorSubject, Observable, Observer } from 'rxjs';

@Injectable({
  providedIn: 'root',
})
export class StreamService {
  primaryCam: BehaviorSubject<any> = new BehaviorSubject<any>(0);
  recording = false;

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

  caputerImage() {
    if (this.recording) {
      this.socket.emit('capture', this.primaryCam.getValue());
    }
  }

  startRecording() {
    if (!this.recording) {
      this.recording = true;
      this.socket.emit('startRecording');
    }
  }

  endRecording() {
    if (this.recording) {
      this.recording = false;
      this.socket.emit('endRecording');
    }
  }
}
