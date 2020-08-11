import { Component, OnInit } from '@angular/core';
import { Run } from '../run';
import { RunService } from '../run.service';

@Component({
  selector: 'app-list',
  templateUrl: './list.component.html',
  styleUrls: ['./list.component.css']
})
export class ListComponent implements OnInit {

  runs: Run[];

  constructor(
    private runService: RunService
  ) { }

  ngOnInit(): void {
    this.getRuns();
  }

  getRuns() {
    this.runService.getFavRuns()
      .subscribe(runs => this.runs = runs)
    console.log("list of runs: ");
    this.runs.forEach(element => {
      console.log(element.name);
    });
  }

}
