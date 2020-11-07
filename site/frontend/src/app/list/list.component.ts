import { Component, OnInit, Input } from '@angular/core';
import { DateHandlerService } from '../date-handler.service';
import { API_URL } from '../env';
import { Run, numHash, Tag } from '../interfaces';
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
    private dateHandlerService: DateHandlerService
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
    this.runService.index = this.id;
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

  deleteTag(runId, target) {
    const runPos = this.getRunIndex(runId);

    this.runService.deleteTag(target).subscribe();

    this.runs[runPos].tags.splice(this.getTagIndex(runPos, target), 1);
  }

  getTagIndex(runID, target) {
    const lambda = (element: Tag) => element.Id === target;
    return this.runs[runID].tags.findIndex(lambda);
  }

  changePrio(target: Run) {
    const index = this.getRunIndex(target.Id);

    this.runs.splice(index, 1);

    if (!target.Tagged) {
      target.Tagged = 1;
      this.runService.allRunsData[0].unshift(target);
    } else {
      target.Tagged = 0;
      if (target.Name) {
        this.runService.allRunsData[1].unshift(target);
      } else this.runService.allRunsData[2].unshift(target);
    }

    this.runService.changePin(target).subscribe();
  }

  setVideo(pipeID, date) {
    const video = `assets/Data/${pipeID}/${this.dateHandlerService.generateDate(
      date
    )}/outputtedVideo.mp4`;
    this.toggleService.setVideo(video);
  }

  getFile(date, pipeID) {
    const strDate = this.dateHandlerService.generateDate(date);
    window.open(`http://${API_URL}/export/folder/${pipeID}!${strDate}`);
  }

  getImage(pipeID, date, targ) {
    const strDate = this.dateHandlerService.generateDate(date);
    window.open(`http://${API_URL}/export/image/${pipeID}!${strDate}!${targ}`);
  }

  exportShape(date, lat, long) {
    const strDate = this.dateHandlerService.generateDate(date);
    window.open(`http://${API_URL}/export/tag/${strDate}b${long}b${lat}b`);
  }
}
