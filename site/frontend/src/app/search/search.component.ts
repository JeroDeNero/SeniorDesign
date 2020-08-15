import { Component, OnInit } from '@angular/core';

import { RunService } from '../run.service';
import { Run } from '../interfaces';

@Component({
  selector: 'app-search',
  templateUrl: './search.component.html',
  styleUrls: ['./search.component.css']
})
export class SearchComponent implements OnInit {

  runs: Run[] = [];

  constructor(
    private runService: RunService
  ) { }

  ngOnInit(): void {
  }


}
