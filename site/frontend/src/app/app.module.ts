import { BrowserModule } from '@angular/platform-browser';
import { HttpClientModule } from '@angular/common/http';
import { FormsModule } from '@angular/forms';
import { NgModule } from '@angular/core';

import { AppComponent } from './app.component';
import { ControlsComponent } from './controls/controls.component';
import { ListComponent } from './list/list.component';
import { FilterOptionsComponent } from './filter-options/filter-options.component';
import { RunPopUpMenuComponent } from './run-pop-up-menu/run-pop-up-menu.component';
import { GetNumOfTags } from './list/getNumOfTags.pipe';
import { MakeDirectory } from './list/makeDirectory.pipe';
import { ServiceWorkerModule } from '@angular/service-worker';
import { environment } from '../environments/environment';
import { EditMenuComponent } from './edit-menu/edit-menu.component';
import { SocketIoModule, SocketIoConfig } from 'ngx-socket-io';
import { API_URL } from './env';
import { SettingsComponent } from './settings/settings.component';

const config: SocketIoConfig = {
  url: API_URL,
  options: { cors_allowed_origins: '*' },
};

@NgModule({
  declarations: [
    AppComponent,
    ControlsComponent,
    ListComponent,
    FilterOptionsComponent,
    RunPopUpMenuComponent,
    GetNumOfTags,
    MakeDirectory,
    EditMenuComponent,
    SettingsComponent,
  ],
  imports: [
    FormsModule,
    BrowserModule,
    HttpClientModule,
    ServiceWorkerModule.register('ngsw-worker.js', {
      enabled: environment.production,
    }),
    SocketIoModule.forRoot(config),
  ],
  providers: [],
  bootstrap: [AppComponent],
})
export class AppModule {}
