import { Component, OnInit } from '@angular/core';

import { RunService } from '../run.service';
import { Run, Tag } from '../run';

@Component({
  selector: 'app-search',
  templateUrl: './search.component.html',
  styleUrls: ['./search.component.css']
})
export class SearchComponent implements OnInit {

  runs: Run[] = []

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
