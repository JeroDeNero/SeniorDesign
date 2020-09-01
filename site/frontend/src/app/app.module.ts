import { BrowserModule } from '@angular/platform-browser';
import { HttpClientModule } from '@angular/common/http';
import { FormsModule } from '@angular/forms'
import { NgModule } from '@angular/core';

import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { ControlsComponent } from './controls/controls.component';
import { SearchComponent } from './search/search.component';
import { FilterComponent } from './filter/filter.component';
import { ListComponent } from './list/list.component';
import { SideMenuComponent } from './side-menu/side-menu.component';
import { FilterOptionsComponent } from './filter-options/filter-options.component';
import { RunPopUpMenuComponent } from './run-pop-up-menu/run-pop-up-menu.component';
import { GetNumOfTags } from './list/getNumOfTags.pipe'


@NgModule({
  declarations: [
    AppComponent,
    ControlsComponent,
    SearchComponent,
    FilterComponent,
    ListComponent,
    SideMenuComponent,
    FilterOptionsComponent,
    RunPopUpMenuComponent,
    GetNumOfTags
  ],
  imports: [
    FormsModule,
    BrowserModule,
    AppRoutingModule,
    HttpClientModule,
  ],
  providers: [],
  bootstrap: [AppComponent]
})



export class AppModule { }
