import { Injectable } from '@angular/core';
import { API_URL } from './env';

@Injectable({
  providedIn: 'root',
})
export class VideoService {
  constructor() {}
}

export function loadBinaryResource() {
  var req = new XMLHttpRequest();
  req.open('GET', `${API_URL}/streams/videoFeed`, false);
  //XHR binary charset opt by Marcus Granado 2006 [http://mgran.blogspot.com]
  req.overrideMimeType('multipart/x-mixed-replace; boundary=frame');
  console.log('stuff here');
  console.log(req.status);
  console.log(req.responseText);
  console.log(req.responseType);
  if (req.status != 200) return '';
  return req.responseText;
}
