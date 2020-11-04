import { Component, OnInit, Input } from '@angular/core';
import { DateHandlerService } from '../date-handler.service';
import { Run, numHash } from '../interfaces';
import { RunService } from '../run.service';
import { ToggleService } from '../toggle.service';

@Component({
  selector: 'app-list',
  templateUrl: './list.component.html',
  styleUrls: ['./list.component.css'],
})
export class ListComponent implements OnInit {
  @Input('id') id: number;
  runs: Run[];
  tagBoxes: numHash;

  constructor(
    private runService: RunService,
    private toggleService: ToggleService,
    private datahandlerService: DateHandlerService
  ) {}

  ngOnInit(): void {
    this.runService.getAllRuns().subscribe((runsList) => {
      this.runs = runsList[this.id];
    });
  }

  toggleTag(target) {
    const index = this.getRunIndex(target);
    this.runs[index].ShowTag = !this.runs[index].ShowTag;
  }

  makeTagVar(target) {
    this.tagBoxes[target] = false;
  }

  editData(target: Run) {
    this.runService.setEditRun(target);
    this.runService.arrayIndex = [this.id, this.getRunIndex(target)];
    this.toggleService.setHideEdit(false);
  }

  deleteRun(target: Run, date: Date, pipeID: String) {
    this.runService.deleteRun(target, date, pipeID).subscribe();

    this.runs.splice(this.getRunIndex(target), 1);
  }

  getRunIndex(target) {
    const lambda = (element: Run) => element.Id === target;
    return this.runs.findIndex(lambda);
  }

  deleteTag(target) {
    this.runService.deleteTag(target).subscribe();
  }

  setVideo(pipeID, date) {
    const video = `assets/Data/${pipeID}/${this.datahandlerService.generateDate(
      date
    )}/outputtedVideo.mp4`;
    this.toggleService.setVideo(video);
  }

  getFile(date, pipeID) {
    const dir = `assets/Data/${pipeID}/${this.datahandlerService.generateDate(
      date
    )}/`;
    this.runService.getFolder(dir);
  }

  exportShape(date, lat, long) {
    this.runService.getShapeFile(date, lat, long).subscribe();
  }
}
