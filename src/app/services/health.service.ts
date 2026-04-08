import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';
import { map, catchError } from 'rxjs/operators';
import { environment } from '../../environments/environment';

export interface HealthResponse {
  version: string;
  timestamp: string;
}

export interface ApiResponse<T> {
  success: boolean;
  data: T;
  timestamp: string;
}

@Injectable({
  providedIn: 'root'
})
export class HealthService {
  private readonly healthUrl = `${environment.apiUrl}/api/v1/health`;

  constructor(private http: HttpClient) {}

  getHealth(): Observable<HealthResponse> {
    return this.http.get<ApiResponse<HealthResponse>>(this.healthUrl).pipe(
      map(resp => resp.data),
      catchError(err => {
        // Propagate error to the caller; no console logging per security rules
        throw err;
      })
    );
  }
}