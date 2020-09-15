import { Component, OnInit, Input } from '@angular/core';
import { Run, numHash } from '../interfaces';
import { RunService } from '../run.service';
import { ToggleService } from '../toggle.service';

@Component({
  selector: 'app-list',
  templateUrl: './list.component.html',
  styleUrls: ['./list.component.css'],
})
export class ListComponent implements OnInit {
  @Input('runs') runs: Run[];
  tagBoxes: numHash;

  constructor(
    private runService: RunService,
    private toggleService: ToggleService
  ) {}

  ngOnInit(): void {}

  toggleTag(target) {
    const index = this.getRunIndex(target);
    this.runs[index].ShowTag = !this.runs[index].ShowTag;
  }

  makeTagVar(target) {
    this.tagBoxes[target] = false;
  }

  editData(target) {
    this.runService.setEditRun(target);
    this.toggleService.setHideEdit(false);
  }

  deleteRun(target) {
    this.runService.deleteRun(target).subscribe();

    this.runs.splice(this.getRunIndex(target), 1);
  }

  getRunIndex(target) {
    const lambda = (element: Run) => element.Id === target;
    return this.runs.findIndex(lambda);
  }

  deleteTag(target) {
    this.runService.deleteTag(target).subscribe();
  }
}
