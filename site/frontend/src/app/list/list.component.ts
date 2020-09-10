import { Component, OnInit, Input } from '@angular/core';
import { Run, numHash } from '../interfaces';
import { RunService } from '../run.service';

@Component({
  selector: 'app-list',
  templateUrl: './list.component.html',
  styleUrls: ['./list.component.css'],
})
export class ListComponent implements OnInit {
  @Input('runs') runs: Run[];
  tagBoxes: numHash;

  constructor(private runService: RunService) {}

  ngOnInit(): void {}

  toggleTags(target) {
    target = !target;
  }

  makeTagVar(target) {
    this.tagBoxes[target] = false;
  }

  editData(target) {
    this.runService.deleteTag(target);
  }

  deleteRun(target) {
    this.runService.deleteRun(target).subscribe();

    console.log(this.runs);

    const lamda = (element: Run) => element.Id === target;
    const index = this.runs.findIndex(lamda);

    console.log('removing: ' + this.runs[index]);

    this.runs.splice(index, 1);

    console.log(this.runs);
  }

  deleteTag(target) {
    this.runService.deleteTag(target).subscribe();
  }
}
