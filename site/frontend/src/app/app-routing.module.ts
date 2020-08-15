import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';
import { SearchComponent } from './search/search.component';
import { FilterComponent } from './filter/filter.component';
import { SideMenuComponent } from './side-menu/side-menu.component';
import { FilterOptionsComponent } from './filter-options/filter-options.component';


const routes: Routes = [
  { path: '', redirectTo: '/search(sideMenu:search)', pathMatch: 'full' },
  { path: 'search', redirectTo: '/search(sideMenu:search)', pathMatch: 'full' },
  { path: 'filter', redirectTo: '/filter(options:filter)', pathMatch: 'full' },
  { path: "search", component: SearchComponent },
  { path: "search", component: SideMenuComponent, outlet: "sideMenu" },
  { path: "filter", component: FilterComponent },
  { path: "filter", component: FilterOptionsComponent, outlet: "options" },
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})

export class AppRoutingModule { }
