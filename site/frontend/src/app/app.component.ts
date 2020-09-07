import { Component, ViewChild } from '@angular/core';
import { VideoService, loadBinaryResource } from './video.service';
import { Observable } from 'rxjs';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css'],
})
export class AppComponent {
  @ViewChild('videoElement') videoElement: any;
  video: any;
  isShown: boolean = false;
  title = 'site';
  primaryCam;

  constructor(private videoService: VideoService) {}

  ngOnInit() {
    this.primaryCam = this.getVideo;
  }

  toggleShow() {
    this.isShown = !this.isShown;
  }

  fillData(runID) {
    if (runID === null) {
      return;
    } else if (runID === 'newRun') {
    }
  }

  getVideo(): Observable<any> {
    return <any>loadBinaryResource();
  }
}
