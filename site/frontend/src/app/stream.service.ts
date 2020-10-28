import { Injectable } from '@angular/core';
import { Socket } from 'ngx-socket-io';
import { BehaviorSubject, Observable, Observer } from 'rxjs';
import { RunService } from './run.service';

@Injectable({
  providedIn: 'root',
})
export class StreamService {
  primaryCam: BehaviorSubject<any> = new BehaviorSubject<any>(0);
  recording = false;

  constructor(private socket: Socket, private runService: RunService) {}

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

  captureImage() {
    if (this.recording) {
      this.socket.emit('capture', this.primaryCam.getValue());
    }
  }

  captureReturn() {
    return new Observable((observer: Observer<any>) => {
      this.socket.on('addTag', (data) => {
        observer.next(data);
      });
    });
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
