import { Injectable } from '@angular/core';
import { HttpClient, HttpHeaders } from '@angular/common/http';

@Injectable({
  providedIn: 'root'
})
export class SalesloftProjectService {
  constructor(private http: HttpClient) {}

  _get_query(url, params) {
    const endpoint =  'http://localhost:8000/api/v2/' + url + 'params={' + params + '&include_paging_counts=true}';
    const  headers = new HttpHeaders(
      {'Authorization': 'Token a83bf6a646e86e95aee5f83eaa1fbfcd9cb4d031'}
    );
    return this.http.get(endpoint,{ headers });
  }

  getPeople(params= null) {
    return this._get_query('people/', params);
  }

  getPeopleUniqueCharacter(params= null) {
    return this._get_query('people-unique-character/', params);
    }
}
